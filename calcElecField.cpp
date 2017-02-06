#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

const double OOFPEZ = 9e9;
const double Q_PROTON = 1.6e-19;
const double Q_ELECTRON = -1 * Q_PROTON;

vector<double> dipole(vector<double> obsLoc, double &magElec);
vector<double> pointCharge(vector<double> obsLoc, vector<double> chargeLoc, bool negCharge, double &magElec);
void readCoordinates(vector<double> &loc);
double getMag(vector<double> vect);

vector<double> operator+(vector<double> v1, vector<double> v2){
  vector<double> returnV;
  for(int i= 0; i < 3; i++) returnV.push_back(v1[i] + v2[i]);
  return returnV;
}

vector<double> operator-(vector<double> v1, vector<double> v2){
  vector<double> returnV;
  for(int i= 0; i < 3; i++) returnV.push_back(v1[i] - v2[i]);
  return returnV;
}

int main(int argc, char* argv[]){
  double choice, magElec;
  vector<double> obsLoc, chargeLoc, eNet;
  char charge;
  cout << "If dipole type 1, if it's just a single charge type 2: ";
  cin >> choice;
  cout << "what is the obsLoc (x, y, z)? ";
  readCoordinates(obsLoc);

  if(choice == 1) {
    eNet = dipole(obsLoc, magElec);
  }
  else {
    cout << "What is the chargeLoc (x, y, z)? ";
    readCoordinates(chargeLoc);
    cout << "Is the charge negative? (y/n): ";
    cin >> charge;
    bool negCharge = (charge == 'y') ? true : false;
    eNet = pointCharge(obsLoc, chargeLoc, negCharge, magElec);
  }
  cout << "eNet = < " << eNet[0] << ", " << eNet[0] << ", " << eNet[2] << "> N/C\n";
  cout << "magElec = " << magElec << " N/C\n";
}

vector<double> dipole(vector<double> obsLoc, double &magElec){
  vector<double> negLoc, posLoc, eNet;
  cout << "Where is the negative charge location (x, y, z)? ";
  readCoordinates(negLoc);
  cout << "Where is the negative charge location (x, y, z)? ";
  readCoordinates(posLoc);
  eNet = pointCharge(obsLoc, negLoc, true, magElec) + pointCharge(obsLoc, posLoc, false, magElec);
  magElec = getMag(eNet);
  return eNet;
}

vector<double> pointCharge(vector<double> obsLoc, vector<double> chargeLoc, bool negCharge, double &magElec){
  vector<double> r, rHat, elecField;
  double magR;
  r = obsLoc - chargeLoc;
  magR =getMag(r);
  rHat.clear();
  for(unsigned int i = 0; i < 3; i++){
    rHat.push_back(r[i]/magR);
    (negCharge) ? elecField.push_back((OOFPEZ*Q_ELECTRON*rHat[i])/pow(magR, 2)) :
                  elecField.push_back((OOFPEZ*Q_PROTON*rHat[i])/pow(magR, 2));
  }
  magElec = getMag(elecField);
  return elecField;
}

double getMag(vector<double> vect){
  return (sqrt(pow(vect[0], 2) + pow(vect[1], 2) + pow(vect[2], 2)));
}

void readCoordinates(vector<double> &loc){
  double x, y, z;
  cin >> x >> y >> z;
  loc.push_back(x);
  loc.push_back(y);
  loc.push_back(z);
}
