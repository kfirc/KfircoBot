from datetime import datetime
from dateutil.relativedelta import relativedelta

from utils import Owner

owner = Owner(
    name='Kfir Cohen',
    age=f'{relativedelta(datetime.utcnow(), datetime(1996, 9, 6)).years} years',
    country='Israel',
    company='At-Bay',
    role='Software Engineer',
)
