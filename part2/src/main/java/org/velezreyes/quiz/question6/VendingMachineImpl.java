package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

    private int insertedMoneyCents = 0;
    private static final int QUARTER_VALUE_CENTS = 25;

    private static VendingMachineImpl instance = new VendingMachineImpl();

    private VendingMachineImpl() {
        // Private constructor for singleton
    }

    public static VendingMachine getInstance() {
        return instance;
    }

    @Override
    public void insertQuarter() {
        insertedMoneyCents += QUARTER_VALUE_CENTS; // Add 25 cents to the inserted money
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        int price = DrinkFactory.getPrice(name);
        if (insertedMoneyCents < price) {
            throw new NotEnoughMoneyException("Inserted money is not enough for " + name + ".");
        }

        // Subtract the price of the drink from the inserted money
        insertedMoneyCents -= price;
        return DrinkFactory.getDrink(name);
    }

    // Additional method to reset the machine for the next user
    public void reset() {
        this.insertedMoneyCents = 0;
    }

    // Additional method to get the current amount of money inserted
    public int getMoneyInserted() {
        return this.insertedMoneyCents;
    }
}
