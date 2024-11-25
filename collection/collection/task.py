class Task:
    def extract(self) -> list[dict]:
        raise NotImplementedError

    def transform(self) -> list[dict]:
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError

    def run(self) -> None:
        df = self.extract()
        df = self.transform(df)
        self.load(df)
