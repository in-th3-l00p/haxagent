from dataclasses import dataclass


@dataclass(frozen=True)
class HackathonRequest:
    name: str
    date: str
    location: str

    def to_prompt(self) -> str:
        return (
            f"index the hackathon '{self.name}' "
            f"happening on {self.date} in {self.location}."
        )
