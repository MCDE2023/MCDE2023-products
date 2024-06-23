import logging
from v1.config.config import Settings, get_config
from v1.model.db_schemas.db_schema import Product, ProductEssential
from v1.model.repository.repository import Repository, Condition
from v1.utils.exception import HttpCustomException, custom_exception_handler
from typing import List, Optional
from v1.model.schemas.schema import GetSchemaProductOut

_config: Settings = get_config()
logger: logging.Logger = logging.getLogger(_config.service_name)
exception_handler = custom_exception_handler()

class ProductsRepository(Repository):
    def __init__(
            self,
            collection_name: str = 'users',
            subcollection_name: str = 'products'
    ) -> None:
        super().__init__(
            collection_name = collection_name,
            subcollection_name = subcollection_name,
        )

    def create_product(self, ID: str, data: Product):
        logger.info("Creates a Product document in Firestore")
        try:
            self._create(ID, data)
            logger.debug(f"Created product document (ID: {ID})")
        except HttpCustomException:
            raise
        except Exception:
            exception_handler.handle_custom_exception(f"An error occurred creating product document (ID: {ID})")


    def get_products(self) -> List[GetSchemaProductOut]:
        try:
            products = self._get_all()

            if products is None:
                logger.info("No products found matching the criteria.")
                return dict()

            return products
        
        except HttpCustomException:
            raise
        except Exception:
            exception_handler.handle_custom_exception(f"Unexpected error retrieving products")


    def get_product(self, ID:str) -> List[GetSchemaProductOut]:
        try:
            product = self._get(ID)

            return product
        
        except HttpCustomException:
            raise
        except Exception:
            exception_handler.handle_custom_exception(f"Unexpected error retrieving products")


    def get_product_byname(self, name:str) -> List[GetSchemaProductOut]:
        try:
            product = self._get_byname(name)

            if product is None:
                logger.info("No products found matching the criteria.")
                return dict()

            return product
        
        except HttpCustomException:
            raise
        except Exception:
            exception_handler.handle_custom_exception(f"Unexpected error retrieving products")

def get_repository() -> ProductsRepository:
    return ProductsRepository()