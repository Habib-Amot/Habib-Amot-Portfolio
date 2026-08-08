MIN_FIELD_WIDTH = 60
heading = "{0:=^"+str(MIN_FIELD_WIDTH)+"}"


def show_heading(topic: str) -> None:
    print(heading.format(topic))