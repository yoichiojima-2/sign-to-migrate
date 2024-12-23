import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collection.task import Task
from utils.utils import get_config, df_to_json


class QualityOfLifeTask(Task):
    output_path = "raw/quality_of_life.json"
    cities = get_config()["cities"]

    @staticmethod
    def get_soup(city: str) -> BeautifulSoup:
        url = f"https://www.numbeo.com/quality-of-life/in/{city}"
        print(f"[QuolityOfLifeTask.scrap] url: {url}")
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.122 Safari/537.36"
            },
        )
        if response.status_code != 200:
            print("status code:", response.status_code)
            print("response headers:", response.headers)
            print("response content:", response.text)
            raise RuntimeError("Failed to fetch data")

        return BeautifulSoup(response.text, "html.parser")

    def scrap(self, city: str) -> pd.DataFrame:
        soup = self.get_soup(city)
        tables = soup.find_all("table")
        qol_table = tables[1]
        other_metrics_tables = tables[2]

        qol_cells = qol_table.find_all("tr")[1].find_all("td")
        data = [
            {
                "feature": qol_cells[0].text.strip(),
                "country": soup.find_all("a", class_="breadcrumb_link")[1].text,
                "city": city,
                "value": float(qol_cells[1].text.strip()),
            }
        ]

        for row in other_metrics_tables.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) > 1:
                data.append(
                    {
                        "feature": cells[0].text.strip().replace("\u0192", "").replace("\u00a0", ""),
                        "country": soup.find_all("a", class_="breadcrumb_link")[1].text,
                        "city": city,
                        "value": float(cells[1].text.strip()),
                    }
                )

        request_interval = 1
        print(f"waiting... {request_interval}s")
        time.sleep(request_interval)
        return pd.DataFrame(data)

    def extract(self) -> pd.DataFrame:
        return pd.concat([self.scrap(city) for city in self.cities])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        keys = ["feature", "country", "city"]
        metrics = ["value"]
        return df[[*keys, *metrics]].groupby(keys).mean().reset_index()

    def load(self, df: pd.DataFrame) -> None:
        df_to_json(df, self.output_path)


if __name__ == "__main__":
    task = QualityOfLifeTask()
    task.run()