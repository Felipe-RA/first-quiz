package org.velezreyes.quiz.question6;

public class NotEnoughMoneyException extends Exception {

  public NotEnoughMoneyException() {
    super("Not enough money inserted.");
  }
  public NotEnoughMoneyException(String message) {
    super(message);
  }
}
