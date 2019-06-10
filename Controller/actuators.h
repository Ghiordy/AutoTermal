/*
 * OOP programming for AutoTermal heat enviroment controller
 * including several devices for heaters and colders
 */

 class actuators{
  // ATRIBUTIONS
  enum kind;
  private:
    enum kind(heater,colder);
  
  public:
  void setKind(enum newKind){
    kind :: newKind;
    }
    
  // BUILDER
  actuators(){
    kind :: heater;
    }
  
  // METHODS
  enum getKind(){
    return kind;
    }
 }
