from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]

        import datetime

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccines is expired")

        if visitor.get("wearing_a_mask") is not True or visitor.get("Wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor is not a wearing mask")

        return f"Welcome to {self.name}"


