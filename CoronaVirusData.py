import matplotlib.pyplot as plt
import warnings
import time
warnings.filterwarnings("ignore", category=UserWarning)
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("https://www.worldometers.info/coronavirus/country/us/")
time.sleep(5)
innerHTML_of_newcases = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[2]/div/script").get_attribute("innerHTML")
index_of_data_initial= innerHTML_of_newcases.index("data: [")
index_of_data_final = innerHTML_of_newcases.index("responsive: {")
data_of_newcases = innerHTML_of_newcases[index_of_data_initial:index_of_data_final].strip()
index1= data_of_newcases.index("[") + 1
index2 = data_of_newcases.index("]")
revised_data= data_of_newcases[index1:index2]
revised_data = revised_data.split(",")
revised_data.remove("null")
for i in range(len(revised_data)):
    revised_data[i] = int(revised_data[i])

plt.plot(revised_data)
plt.title("Daily Cases")
plt.xlabel("Day Since Beginning Of COVID-19")
plt.ylabel("New Cases")
plt.show()








