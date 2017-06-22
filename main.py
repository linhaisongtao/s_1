import model
import source
import processor

print "Hello today is", model.now_date

selected_stock_map = source.convert_selected_codes_to_map(source.get_selected_stocks())

stock_list = source.get_lixinger_stocks()
stock_list = processor.process(stock_list)

l = processor.process(stock_list)
model.write_to_excel(l, "lixinger_all_" + model.now_date + ".xls")

l = processor.selectStocks(selected_stock_map, stock_list)
model.write_to_excel(l, "lixinger_my_" + model.now_date + ".xls")

print "ok, bye!"
