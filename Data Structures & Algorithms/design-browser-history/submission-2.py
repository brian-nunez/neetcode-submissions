class BrowserHistory:

    def __init__(self, homepage: str):
        self.history: List[str] = [homepage]
        self.current: int = 0
        self.end = 0

    def visit(self, url: str) -> None:
        if len(self.history) > self.current + 1:
            self.history[self.current+1] = url
        else:
            self.history.append(url)
        self.current += 1
        self.end = self.current


    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.end, self.current + steps)
        return self.history[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)