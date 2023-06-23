from dataclasses import dataclass, field


@dataclass
class MongoConfig:
    HOST: str = "localhost"
    PORT: int = 27017
    USERNAME: str = "felipedmnq"
    PASSWORD: str = "felipedmnq"
    DB_NAME: str = "test_db"
    EDIT_OPERATORS: dict = field(
        default_factory=lambda: {
            "set": "$set",
            "inc": "$inc",
            "mul": "$mul",
            "rename": "$rename",
            "unset": "$unset",
            "min": "$min",
            "max": "$max",
            "current_date": "$currentDate",
            "add_to_set": "$addToSet",
            "pop": "$pop",
            "pull": "$pull",
            "push": "$push",
            "push_all": "$pushAll",
            "each": "$each",
            "slice": "$slice",
            "sort": "$sort",
            "position": "$position",
            "bit": "$bit",
        }
    )
