from typing import Annotated, Literal
from pydantic import BaseModel, Field, ConfigDict

class Observation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    Gender: str
    Customer_Type: str = Field(alias="Customer Type")
    Age: int
    Type_of_Travel: str = Field(alias="Type of Travel")
    Class: str
    Flight_Distance: int = Field(alias="Flight Distance")
    
    # For the rating columns, we combine the alias with the Annotated validation
    Inflight_wifi_service: Annotated[int, Field(ge=1, le=5, alias="Inflight wifi service")]
    Departure_Arrival_time_convenient: Annotated[int, Field(ge=1, le=5, alias="Departure/Arrival time convenient")]
    Ease_of_Online_booking: Annotated[int, Field(ge=1, le=5, alias="Ease of Online booking")]
    Gate_location: Annotated[int, Field(ge=1, le=5, alias="Gate location")]
    Food_and_drink: Annotated[int, Field(ge=1, le=5, alias="Food and drink")]
    Online_boarding: Annotated[int, Field(ge=1, le=5, alias="Online boarding")]
    Seat_comfort: Annotated[int, Field(ge=1, le=5, alias="Seat comfort")]
    Inflight_entertainment: Annotated[int, Field(ge=1, le=5, alias="Inflight entertainment")]
    On_board_service: Annotated[int, Field(ge=1, le=5, alias="On-board service")]
    Leg_room_service: Annotated[int, Field(ge=1, le=5, alias="Leg room service")]
    Baggage_handling: Annotated[int, Field(ge=1, le=5, alias="Baggage handling")]
    Checkin_service: Annotated[int, Field(ge=1, le=5, alias="Checkin service")]
    Inflight_service: Annotated[int, Field(ge=1, le=5, alias="Inflight service")]
    Cleanliness: Annotated[int, Field(ge=1, le=5, alias="Cleanliness")]
    
    Departure_Delay_in_Minutes: int = Field(alias="Departure Delay in Minutes")
    Arrival_Delay_in_Minutes: float = Field(alias="Arrival Delay in Minutes")

class Prediction(BaseModel):
    prediction: Literal["satisfied", "neutral or dissatisfied"]