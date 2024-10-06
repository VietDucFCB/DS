from mrjob.job import MRJob

class MRMaxRevenueYear(MRJob):

    def mapper(self, _, line):
        # Tách dòng thành các phần tử
        data = line.split(',')

        if data[0] == 'product_id':
            return
        if len(data) == 3:
            try:
                product_id, year, revenue = data[0], int(data[1]), float(data[2])
                # Phát ra cặp khóa-giá trị (product_id, (year, revenue))
                yield (product_id, (year, revenue))
            except ValueError:
                # Bỏ qua dòng nếu dữ liệu không hợp lệ
                pass

    def reducer(self, key, values):
        # Tìm năm có doanh thu cao nhất cho từng sản phẩm
        max_year, max_revenue = None, 0
        for year, revenue in values:
            if revenue > max_revenue:
                max_year, max_revenue = year, revenue
        # Phát ra cặp (product_id, (max_year, max_revenue))
        yield (key, (max_year, max_revenue))

if __name__ == '__main__':
    MRMaxRevenueYear.run()
