package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class DrinkFactory {

    // Mapping the enum drink brands to the Drink objects
    private static final Map<DrinkBrand, Drink> drinkMap = new HashMap<>();

    static {
        // Populate the drinkMap with DrinkBrand and corresponding Drink instances

        drinkMap.put(DrinkBrand.SCOTTCOLA, new DrinkImpl("ScottCola", true));
        drinkMap.put(DrinkBrand.KARENTEA, new DrinkImpl("KarenTea", false));
        // you can add more drinks herre  ...!!!
    }

    public static Drink getDrink(String name) throws UnknownDrinkException {
        // Convert the name to a DrinkBrand enum, this will throw IllegalArgumentException
        // if the name does not correspond to any enum constant.

        try {
            DrinkBrand brand = DrinkBrand.valueOf(name.toUpperCase().replace(" ", "_"));
            return drinkMap.get(brand);
        } catch (IllegalArgumentException e) {
            // If the name is not valid, throw UnknownDrinkException with cute custom message UwU
            throw new UnknownDrinkException("The drink " + name + " is not available.");
        }
    }





}
