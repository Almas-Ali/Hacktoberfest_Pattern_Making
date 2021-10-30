// Using stream api in java8 , to map out a particular field value from a list of objects, and collect field values as list

import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.stream.Collectors;

class Car {
	private String name;
	private String brand;

	public Car(String a, String b){
		this.name = a;
		this.brand = b;
	}

	public String getName(){
		return this.name;	
	}
}

class JavaStreamsExample1
{
	public static void main (String[] args) throws java.lang.Exception
	{

		List<Car> list = new ArrayList();

		list.add(new Car("beetle", "VW"));
		list.add(new Car("mustang", "Ford"));

		List<String> carnames = list.stream().map(Car::getName).collect(Collectors.toList());

		for(String name : carnames){
			System.out.println(name);
		}
	}
}



/**
Success	output #stdout
beetle
mustang
*/
