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

    public static Drink getDrink(String name) throws UnknownDrinkException 
    {
        // Convert the name to a DrinkBrand enum, 
        // this will throw IllegalArgumentException if it does not exist.

        try {
            DrinkBrand brand = DrinkBrand.valueOf(name.toUpperCase().replace(" ", "_"));
            return drinkMap.get(brand);
        } catch (IllegalArgumentException e) {
            // If the name is not valid, throw UnknownDrinkException with cute custom message UwU
            throw new UnknownDrinkException("The drink " + name + " is not available.");
        }
    }

    public static int getPrice(String name) throws UnknownDrinkException {
        try {
            DrinkBrand brand = DrinkBrand.valueOf(name.toUpperCase().replace(" ", "_"));
            // Logic to determine the price of the drink
            switch (brand) {
                case SCOTTCOLA:
                    return 75; // price in cents
                case KARENTEA:
                    return 100; // price in cents
                default:
                    // this will never happen
                    throw new UnknownDrinkException("The price for " + name + " is unknown.");
            }
        } catch (IllegalArgumentException e) {
            throw new UnknownDrinkException("The price for " + name + " is unknown.");
        }
    }
    




}
