class MyStack(object):

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_2.append(x)
        while self.queue_1:
            self.queue_2.append(self.queue_1.pop(0))
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1



    def pop(self):
        """
        :rtype: int
        """
        return self.queue_1.pop(0)


    def top(self):
        """
        :rtype: int
        """
        return self.queue_1[0]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue_1 and not self.queue_2