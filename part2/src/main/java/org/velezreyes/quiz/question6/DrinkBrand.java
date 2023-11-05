package org.velezreyes.quiz.question6;

public enum DrinkBrand{
    SCOTTCOLA("ScottCola", 75),
    KARENTEA("KarenTea", 100);
    
    // space for other Drink brands!

    private final String displayName;
    private final int price;

    DrinkBrand(String displayName, int price) {
        this.displayName = displayName;
        this.price = price;
    }

    public String getDisplayName() {
        return displayName;
    }

    public int getPrice() {
        return price;
    }
}