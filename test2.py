import uuid

# print(uuid.uuid4())

print(str(uuid.uuid4())[-5:] + str(uuid.uuid4())[:4])
