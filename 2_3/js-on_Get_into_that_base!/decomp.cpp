int main() 
{
	timeval tv;
	gettimeofday(&tv, 0);

	auto tv_sec = tv.tv_sec;
	auto tv_usec = tv.tv_usec;

	signed int a = (signed int)((double)(tv_sec * 1000) + (tv_usec / 1000L));

	int tv_usec_sum = cross_sum(tv_usec);
	auto b = tv_usec_sum * tv_usec;
	auto r = a % b;

	int input;
	std::cin >> input;
	
	if (input != r) return 1;
	return 0;
}

int cross_sum(int n)
{
	auto ln_n = log(n);
	const int LN_10 = log(10);
	auto n_digit_cnt = (ln_n / LN_10) + 1;

	int acc = 0;

	for (int i = 0; i < n_digit_count; i++) 
	{
		auto r = n % p(10, i);
		auto r1 = (n-r) % p(10, i+1);
		auto v = r1 / p(10, i);
		acc += v;
	}

	return acc; 
}

long p(int a, int b) 
{
	long val = a;
	for (int i = 1; i < b; i++) 
	{
		val *= a;
	}

	return val;
}
