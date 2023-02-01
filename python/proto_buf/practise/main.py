import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumeration_pb2 as enumeration_pb2


def simple():
    return simple_pb2.Simple(
        id=1,
        is_simple=True,
        name="My Name",
        sample_lists=[1, 2, 3],
    )


def complex():
    message = complex_pb2.Complex()
    message.one_dummy.id = 1
    message.one_dummy.name = "My Name"
    message.multiple_dummies.add(id=2, name="Multiple 1")
    message.multiple_dummies.add(id=3, name="Multiple 2")
    message.multiple_dummies.add(id=4, name="Multiple 3")
    message.multiple_dummies.add(id=5, name="Multiple 4")
    return message


def enums():
    return enumeration_pb2.Enumeration(
        # eye_color=enumeration_pb2.EYE_COLOR_BLUE,
        eye_color=1,
    )


if __name__ == "__main__":
    # print(simple())
    print(complex())
    print(enums())
