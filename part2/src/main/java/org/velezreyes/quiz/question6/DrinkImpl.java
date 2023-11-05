package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink {
    private final String name;
    private final boolean fizzy;

    public DrinkImpl(String name, boolean fizzy) {
        this.name = name;
        this.fizzy = fizzy;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return fizzy;
    }
}