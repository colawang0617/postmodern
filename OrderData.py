class OrderData:
    pincode = None
    order_Item = None
    open_status = None
    box_id = None

    def __init__(self, pincode, order_item, open_status, box_id):
        self.pincode = pincode
        self.order_Item = order_item
        self.open_status = open_status
        self.box_id = box_id
