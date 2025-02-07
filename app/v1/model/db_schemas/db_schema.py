# Define a model for your DB data (pydantic model)
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

class ProductEssential(BaseModel):
    name:        str                        # Name of the product	
    description: str                        # Detailed description of the product	
    category_id: Optional[str] = None       # id for the category of the product
    brand_id:    Optional[str] = None       # id for the brand of the product
    price:       float                      # Price of the product
    weight:      Optional[float] = None     # Weight of the product
    created_at:  str                   # Date and time the product was created

    model_config = ConfigDict(
    from_attributes=True,
    )

class Product(ProductEssential):
    ID:  str                                         # Unique identifier for the product
    updated_at:  Optional[str] = None                   # Date and time the product was last updated

    model_config = ConfigDict(
    from_attributes=True,
    )