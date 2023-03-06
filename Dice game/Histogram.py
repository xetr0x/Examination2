class Histogram:

    def init(self, values):
        self.histogram = {}
        for value in values:
            if value not in self.histogram:
                self.histogram[value] = 1
        else:
            self.histogram[value] += 1

    def get_str(self):
        str_list = []
        for value, count in self.histogram.items():
            str_list.append(f"{value}: {count}")
        return "\n".join(str_list)
