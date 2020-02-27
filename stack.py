class stack():
    def __init__(self):
        self.data_ = []
        self.size_ = 0
        self.max_size_ = 100

    def is_empty(self) -> bool:
        return (self.size_ == 0)

    def size_of(self) -> int:
        return len(self.data_)

    def pop(self) -> float:
        if(self.is_empty()):
          print("cannot pop value, stack is empty!")
          return None
        self.size_-=1
        return self.data_[self.size_]

    def peek(self) -> float:
        if(self.is_empty()):
          print("cannot peek value, stack is empty!")
          return None
        return self.data_[self.size_-1]

    def push(self, value: float) -> None:
        self.size_+=1
        if(self.size_ >= self.max_size_):
          print("cannot push value to the stack, it is full!")
          return
        self.data_.append(value)
    def clear_contents(self) -> None:
        self.data_.clear()
        self.size_ = 0
