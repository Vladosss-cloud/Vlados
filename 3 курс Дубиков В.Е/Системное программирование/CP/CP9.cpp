#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

struct Date {
	int day;
	int month;
	int year;
};

// Проверка, является ли дата весенней
bool isSpringDate(const Date& date) {
	return (date.month == 3 && date.day >= 1) ||   // Март
	(date.month == 4) ||                   // Апрель
	(date.month == 5 && date.day <= 31);    // Май (до 31 числа)
}

// Чтение дат из файла
vector<Date> readDatesFromFile(const string& filename) {
	vector<Date> dates;
	ifstream file(filename);
	string line;
	
	if (!file.is_open()) {
		cerr << "Ошибка открытия файла!" << endl;
		return dates;
	}
	
	while (getline(file, line)) {
		istringstream iss(line);
		Date date;
		char sep; // разделитель (например, '/', '.', '-')
		if (iss >> date.day >> sep >> date.month >> sep >> date.year) {
			dates.push_back(date);
		}
	}
	
	file.close();
	return dates;
}

int main() {
	string filename = "dates.txt"; // Укажите имя файла
	vector<Date> dates = readDatesFromFile(filename);
	
	cout << "Весенние даты:" << endl;
	for (const auto& date : dates) {
		if (isSpringDate(date)) {
			cout << date.day << "." << date.month << "." << date.year << endl;
		}
	}
	
	return 0;
}
