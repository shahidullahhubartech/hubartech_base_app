from azure.servicebus import ServiceBusClient, AutoLockRenewer
# from django.conf import settings

AZURE_EVENT_ENDPOINT = "Endpoint=sb://exos-test-service-bus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=YtwVKoCsyCFDM8If9D/glLkspgMx5TiEKiJuo96vz7w="
QUEUE_NAME = "testqueue"
CONNECTION_STR = AZURE_EVENT_ENDPOINT


servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR)

with servicebus_client:
    # get the Queue Receiver object for the queue
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg))
            # complete the message so that the message is removed from the queue
            receiver.complete_message(msg)
            messages = receiver.peek_messages()
            for msg in messages:
                print(str(msg))