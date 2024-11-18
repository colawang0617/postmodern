class OrderData:
    pincode = None
    order_Item = None
    open_status = None
    box_id = None

    def __init__(self, query_result):
        self.pincode = query_result.get("Pincode")
        self.order_Item = query_result.get("Order_Item")
        self.open_status = query_result.get("Open_status")
        self.box_id = query_result.get("Box_id")
