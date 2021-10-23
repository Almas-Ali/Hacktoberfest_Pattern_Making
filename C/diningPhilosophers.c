#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
#include<Windows.h>

//SABIT DEGISKEN TANIMLAMALARI//
#define N 5
#define LEFT i>0?(i-1)%N:N-1 // Sol tarafimizdaki indis icin(i) i 0 dan buyukse i degerinden 1 cikartip mod N(5) aliriz, degilse N degerinden 1 cikarip isleme devam ederiz.
#define RIGHT (i+1)%N // Sag tarafimizdaki indis icin i ye 1 ekler mod(N) 5'ini aliriz
#define THINKING 0
#define HUNGRY 1
#define EATING 2

//GLOBAL DEGER TANIMLAMALARI//
int state[N];
int philosopher_num[N];
//SEMAPHORE TANIMLAMALARI//
sem_t mutex;
sem_t sem_phil[N];


//FONKSIYON TANIMLAMALARI//
void *philosopher(void *);
void takechops(int);
void putchops(int);
void eat(int);

int main(int argc,char *arg[]){
	int k;
	pthread_t tid[N];
	printf("***************Phiosophers on the Dining***************\n");
	Sleep(1000);
	for(k=0;k<N;k++) philosopher_num[k]=k;			//Filozof tanimlamasi icin for dongusu 1. filozof 2. filozof...
	sem_init(&mutex,0,1);//binary semaphore tanimlamasi ve mutex semp. 1 degeri atanmis olur.
	for(k=0;k<N;k++) sem_init(&sem_phil[k],0,0); // Binary semafor.
	for(k=0;k<N;k++) pthread_create(&tid[k],NULL,philosopher,&philosopher_num[k]);//Her filozof icin 1 adet thread yaratiyor ve onun bilgilerini tutuyoruz.
	//Threadin cikmasi icin bekliyoruz...
	for(k=0;k<N;k++) pthread_join(tid[k],NULL); // Fork-join stratejisi icin. Problemi bol sonra birlestir. Daha performansli calismasi icin. 
	return 0;
}

void *philosopher(void *param){
	int i=*((int *)param); //Filozofun indisi hangi filozof oldugu i degerine aktarilir.
	int counter = 0;
	while(1){
		Sleep(1);
		takechops(i);
		Sleep(2);
		putchops(i);
		counter++;
		if(counter == 1)
			break;
	}
}

void takechops(int i){
	sem_wait(&mutex); // mutex semaforunu wait durumuna sokar. 
	state[i]=HUNGRY;
	printf("Philosopher %d is hungry\n",i);
	eat(i);
	sem_post(&mutex);// mutex semaforunu signal durumuna gecirir.
	sem_wait(&sem_phil[i]);// semaforunu wait durumuna gecirir. 
}
void putchops(int i){
	sem_wait(&mutex);
	state[i]=THINKING;
	printf("Philosopher %d is thinking\n",i);
	eat(LEFT);
	eat(RIGHT);
	sem_post(&mutex);
}
void eat(int i){
	if(state[i] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING){
		state[i]=2;
		printf("Philosopher %d is eating\n",i);
		sem_post(&sem_phil[i]);//semaphore'u signal yapar. 
	}
}
