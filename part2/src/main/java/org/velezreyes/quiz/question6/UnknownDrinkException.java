package org.velezreyes.quiz.question6;

public class UnknownDrinkException extends Exception {

  public UnknownDrinkException() {
    super("Unknown drink!");
  }

  public UnknownDrinkException(String message) {
    super(message);
  }
}
