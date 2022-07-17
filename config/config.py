from dataclasses import dataclass


@dataclass
class Config:
    token: str
    port: int
    url: str
    cert: str
    key: str

    def hook_url(self) -> str:
        return f"{self.url}:{self.port}/{self.token}"
