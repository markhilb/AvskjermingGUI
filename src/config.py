from decimal import Decimal

PAD_X = 50

CANVAS_BASELINE = Decimal('300')

WALLMOUNT_SCALE = Decimal('6')
POST_SCALE = Decimal('2')
GLASS_SCALE = Decimal('1')

GLASS_WEIGHT_MULTIPLYER = Decimal('0.5')
WALLMOUNT_WEIGHT_MULTIPLYER = Decimal('0.2')
POST_WEIGHT_MULTIPLYER = Decimal('0.3')

WALLMOUNT_WIDTH = Decimal('0.5')
POST_WIDTH = Decimal('1.3')
POST_BASE_WIDTH = Decimal('2')
POST_BASE_HEIGHT = Decimal('2')
POST_LAST_WIDTH = POST_WIDTH + POST_BASE_WIDTH

GLASS_BASELINE = CANVAS_BASELINE - POST_BASE_HEIGHT

LENGTH_BAR_SIDES_TOP = Decimal('320')
LENGTH_BAR_SIDES_HEIGHT = Decimal('10')
LENGTH_BAR_THICKNESS = Decimal('1')
LENGTH_BAR_SIDES_BOTTOM = LENGTH_BAR_SIDES_TOP + LENGTH_BAR_SIDES_HEIGHT
LENGTH_BAR_TOP = LENGTH_BAR_SIDES_TOP + (LENGTH_BAR_SIDES_HEIGHT / 2)
LENGTH_BAR_BOTTOM = LENGTH_BAR_TOP + LENGTH_BAR_THICKNESS
LENGT_BAR_LABEL_TOP = LENGTH_BAR_SIDES_TOP + LENGTH_BAR_SIDES_HEIGHT + 5