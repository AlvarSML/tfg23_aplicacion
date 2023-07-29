# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.model import Model  # noqa
#from app.models.regression_model import RegressionModel  # noqa
#from app.models.segmentation_model import SegmentationModel  # noqa
from app.models.regseg_model import RegressionModel, SegmentationModel