class Stack:

    def __init__(self, size: int) -> None:
        self.stack: List[Any] = []
        self.size = size

    def __repr__(self) -> str:
        return str(self.stack)

    def add(self, elem: Any) -> None:
        if len(self.stack) >= self.size:
            raise ValueError('The Stack is full')

        self.stack.append(elem)

    def remove(self) -> Any:
        if not self.stack:
            raise ValueError('The Stack is empty')

        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0