#include <stdio.h>
#include <stdlib.h>

int main (int argc, char * argv[]) {
	FILE *fi, *fo;
	int pos = 0;
	char line[100];
	if (argc<4) {
		printf("Usage: %s <infile> <outfile> <bit position>\n", argv[0]);
		return 1;
	}
	if (1 != sscanf(argv[3], "%d", &pos)) {
		printf("Error: Bit position is not a decimal integer.\nUsage: %s <infile> <outfile> <bit position>\n", argv[0]);
		return 1;
	}
	
	fi = fopen(argv[1], "rt");
	if (!fi) {
		printf("Unable to open input file %s.\n", argv[1]);
		perror("Error: ");
		return 1;
	}
	fo = fopen(argv[2], "wb");
	if (!fo) {
		printf("Unable to open output file %s.\n", argv[2]);
		perror("Error: ");
		return 1;
	}
	unsigned num, bi;
	int i = 0;
	while (!feof(fi)) {
		fscanf(fi, "%04x\n", &num);
		bi = (num & (1 << pos)) >> pos;
		fprintf(fo, "%d", bi);
		i++;
		if (i % 100 == 0) { printf("i=%d: %04x  \r",i,num); }
	}
	puts("");
	fclose(fi);
	fclose(fo);
}
