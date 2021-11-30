#include <iostream>
#include <unordered_map>

using std::string;

// Housetype Design Pattern
//
// Intent: Lets you copy existing objects without making your code dependent on
// their classes.

enum Type {
  HOUSE_SOFT = 0,
  HOUSE_CHANGE
};

/**
 * The example class that has cloning ability. We'll see how the values of field
 * with different types will be cloned.
 */

class Housetype {
 protected:
  string prototype_name_;
  float prototype_field_;

 public:
  Housetype() {}
  Housetype(string housetype_name)
      : prototype_name_(housetype_name) {
  }
  virtual ~Housetype() {}
  virtual Housetype *Clone() const = 0;
  virtual void HousetypeFunction(float prototype_field) {
    this->prototype_field_ = prototype_field;
    std::cout << "Build HousetypeFunction from " << prototype_name_ << " with money : " << prototype_field << "万" << std::endl;
  }
};

/**
 * HouseSoft is a Sub-Class of Housetype and implement the Clone HousetypeFunction
 * In this example all data members of Housetype Class are in the Stack. If you
 * have pointers in your properties for ex: String* name_ ,you will need to
 * implement the Copy-Constructor to make sure you have a deep copy from the
 * clone HousetypeFunction
 */

class HouseSoft : public Housetype {
 private:
  float housetype_field1_;

 public:
  HouseSoft(string housetype_name, float housetype_field)
      : Housetype(housetype_name), housetype_field1_(housetype_field) {
  }

  /**
   * Notice that Clone HousetypeFunction return a Pointer to a new HouseSoft
   * replica. so, the client (who call the clone HousetypeFunction) has the responsability
   * to free that memory. I you have smart pointer knowledge you may prefer to
   * use unique_pointer here.
   */
  Housetype *Clone() const override {
    return new HouseSoft(*this);
  }
};

class HouseChange : public Housetype {
 private:
  float housetype_field2_;

 public:
  HouseChange(string housetype_name, float housetype_field)
      : Housetype(housetype_name), housetype_field2_(housetype_field) {
  }
  Housetype *Clone() const override {
    return new HouseChange(*this);     //*this=object1,    return object2; *this=object1,    return object3
  }
};

/**
 * In HousetypeFactory you have two concrete prototypes, one for each concrete
 * Housetype class, so each time you want to create a bullet , you can use the
 * existing ones and clone those.
 */

class HousetypeFactory {
 private:
  std::unordered_map<Type, Housetype *, std::hash<int>> housetype_;

 public:
  HousetypeFactory() {
    housetype_[Type::HOUSE_SOFT] = new HouseSoft("HOUSE_SOFT ", 50.f);
    housetype_[Type::HOUSE_CHANGE] = new HouseChange("HOUSE_CHANGE ", 60.f); //object1
  }

  /**
   * Be carefull of free all memory allocated. Again, if you have smart pointers
   * knowelege will be better to use it here.
   */

  ~HousetypeFactory() {
    delete housetype_[Type::HOUSE_SOFT];
    delete housetype_[Type::HOUSE_CHANGE];
  }

  /**
   * Notice here that you just need to specify the type of the Housetype you
   * want and the HousetypeFunction will create from the object with this type.
   */
  Housetype *CreateHousetype(Type type) {
    return housetype_[type]->Clone();
  }
};

void Client(HousetypeFactory &prototype_factory) {
  std::cout << "Let's create a Housetype 1\n";
  /*
  Housetype *Housetype1= new HouseSoft("HOUSE_SOFT ", 50.f);
  Housetype *HousetypeNew1(*Housetype1);
  Housetype1->HousetypeFunction(90);
  */

  Housetype *Housetype = prototype_factory.CreateHousetype(Type::HOUSE_SOFT);
  Housetype->HousetypeFunction(90);
  delete Housetype;

  std::cout << "\n";
  std::cout << "Let's create a Housetype 2 \n";

  Housetype = prototype_factory.CreateHousetype(Type::HOUSE_CHANGE);
  Housetype->HousetypeFunction(10);

  Housetype = prototype_factory.CreateHousetype(Type::HOUSE_CHANGE);
  Housetype->HousetypeFunction(20);

  delete Housetype;
}

int main() {
  HousetypeFactory *prototype_factory = new HousetypeFactory();
  Client(*prototype_factory);
  delete prototype_factory;

  return 0;
}