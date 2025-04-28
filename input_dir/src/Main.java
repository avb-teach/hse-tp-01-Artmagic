import javax.naming.InvalidNameException;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;
import java.util.Map;

class Main {

        static Map<String, Integer> variables;

        public Main() {
            variables = new HashMap<>();
            variables.put("x1", 0);
            variables.put("x2", 0);
            variables.put("x3", 0);
            variables.put("x4", 0);
            variables.put("x5", 0);
        }


        public static int operation(int a, int b, String expression){
            if (expression.equals("+")) return a + b;
            else if (expression.equals("-")) return a - b;
            else if (expression.equals("*")) return a * b;
            else if (expression.equals("/")){
                if(b == 0) {
                    throw new ArithmeticException("Ошибка. Деление на ноль");
                } else {
                    return a/b;
                }
            }
            else{
                throw new ArithmeticException("Неизвестный токен '" + expression + "'");
            }
        }

        public static int postfix_notation(String[] values) {
        Stack<Integer> stack = new Stack<>();
        String operators = "+-*/";

        for (String value : values) {
            if (operators.contains(value)) {
                if (stack.size() < 2) {
                    throw new IllegalArgumentException("Недостаточно операндов для операции '" + value + "'");
                }
                int b = stack.pop();
                int a = stack.pop();
                stack.push(operation(a, b, value));
            } else if (variables.containsKey(value)) {
                stack.push(variables.get(value));
            } else {
                try {
                    stack.push(Integer.valueOf(value));
                } catch (NumberFormatException e) {
                    throw new IllegalArgumentException("Неизвестный токен '" + value + "'");
                }
            }
        }
        if (stack.size() != 1) {
            throw new IllegalArgumentException("Недостаточно операндов для вычисления.");
            }
            return stack.pop();
        }

        public static int postfix_notation_assignation(String input) {
            String[] parts = input.split("=");

            if (parts.length != 2){
                throw new IllegalArgumentException("Ошибка присваивания");
            }

            String varibleName = parts[0].trim();
            String varibleNotation = parts[1].trim();

            int value = postfix_notation(varibleNotation.split(" "));

            variables.put(varibleName, value);
            return value;
        }
    public static void main(String[] args) {
        Main calculator = new Main();
        Scanner input = new Scanner(System.in);
        System.out.println("Вводите запись в обратной польской нотации (для выхода введите quit):");


        while (true) {
            try {
                String expression = input.nextLine();

                if(expression.matches("[/*+-].*")){
                    throw new IllegalArgumentException("Неверный порядок действий");
                }
                if(expression.equals("quit")){
                    break;
                }

                if (expression.contains("=")) {
                    int result = postfix_notation_assignation(expression);
                    System.out.println(result);
                } else {
                    int result = postfix_notation(expression.split(" "));
                    System.out.println(result);
                }

            } catch (Exception e){
                System.out.println(e.getMessage());
            }
        }
    }
}