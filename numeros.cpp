#include <iostream>
int main(){
    int i;
    char salir;
        for (i=1;i<=10;i++){
        std::cout<<i;
        std::cout<<"\n";
        }
        std::cout<<"Toca cualquier letra para salir";
        std::cin>>salir;
        return 0;
}
