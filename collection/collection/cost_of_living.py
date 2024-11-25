import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collection.task import Task


class CostOfLivingTask(Task):
    cities = [
        "Tokyo",
        "London",
        "New-York",
        "Brisbane",
        "Bristol",
        "Manchester",
        "Mumbai",
        "Bangkok",
        "Kuala-Lumpur",
        "Singapore",
        "Taipei",
        "Shanghai",
        "Hong-Kong",
    ]

    @staticmethod
    def _scrap(city: str, currency: str = "JPY") -> pd.DataFrame:
        url = f"https://www.numbeo.com/cost-of-living/in/{city}?displayCurrency={currency}"
        print(f"[CostOfLivingTask._scrap] url: {url}")
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.122 Safari/537.36"
            },
        )
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find("table", {"class": "data_wide_table"}).find_all("tr")
        cost = []
        for row in rows:
            cells = row.find_all("td")
            if len(cells) > 1:
                cost.append(
                    {
                        "item": cells[0].text.strip(),
                        "country": soup.find_all("a", class_="breadcrumb_link")[1].text,
                        "city": city,
                        "currency": currency,
                        "cost": float(cells[1].text.strip().replace("\xa0¥", "").replace(",", "")),
                    }
                )

        return pd.DataFrame(cost)

    def extract(self) -> pd.DataFrame:
        return pd.concat([self._scrap(city) for city in self.cities])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        keys = ["item", "country", "city"]
        metrics = ["cost"]
        return df[[*keys, *metrics]].groupby(keys).mean().reset_index()

    def load(self, df: pd.DataFrame) -> pd.DataFrame:
        df.to_json(Path(os.getenv("DATA_DIR")) / "cost_of_living.json", orient="records", index=False)


if __name__ == "__main__":
    task = CostOfLivingTask()
    task.run()
