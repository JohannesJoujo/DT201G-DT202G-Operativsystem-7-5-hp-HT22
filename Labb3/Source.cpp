//Johannes Joujo
#include <iostream>
#include <chrono>
void menu();
void insert(int in);

int main() {
	menu();
	return 0;
}

void menu() {
	std::cout << "what do you want to test: \n";
	std::cout << "1: KiB \n";
	std::cout << "2: Gb\n";
	int input = 0;
	std::cin >> input;
	insert(input);

}


void insert(int in) {
	int count = 0;

	int64_t Alokerat = 0;
	int KiB = pow(2, 10) / sizeof(int64_t);
	int Gb = pow(2, 30) / sizeof(int64_t);

	if (in == 1) {
		auto start = std::chrono::high_resolution_clock::now();

		try {

			while (1) {
				new int64_t[KiB];
				Alokerat += KiB * sizeof(int64_t);
				count++;
				if (count == 1024)
				{
					std::cout << Alokerat << "\n";
					count = 0;
				}

			}
		}
		catch (std::bad_alloc& e) {
			std::cout << "proroblemmmmm! " << e.what();
			auto stop1 = std::chrono::high_resolution_clock::now();
			auto tid = std::chrono::duration<double>(stop1 - start);
			std::cout << "\nTime taken: "<< tid.count() << " seconds" << std::endl;
		}

	}
	else if (in == 2) {
		auto start2 = std::chrono::high_resolution_clock::now();
		
		try {
			while (1) {

				new int64_t[Gb];
				Alokerat += Gb * sizeof(int64_t);


				std::cout << Alokerat << "\n";


			}
		}
		catch (std::bad_alloc& e) {
			std::cout << "proroblemmmmm! " << e.what();
			auto stop2 = std::chrono::high_resolution_clock::now();
			auto tid = std::chrono::duration<double>(stop2 - start2);
			std::cout << "\nTime taken: "<< tid.count() << " seconds" << std::endl;
		}
	}

}