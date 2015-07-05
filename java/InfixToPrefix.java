/* *************************************************
 * Convert an infix arithmetic expression to prefix.
 * Ex. (8+2)/5*(6^2+1-8/2) to 8 2 + 5 / 6 2 ^ 1 + 8 2 / - *
 *
 * Precedence of math operators is PEMDAS (paren, exp, mul, div, add, sub).
 *
 * A typical programming problem in introductory data structures courses
 * to introduce stack data structure.
 * Also, an interview question from Twitch.
 *
 * ************************************************** */

import java.util.List;
import java.util.ArrayList;

import java.io.IOException;
import java.io.StreamTokenizer;
import java.io.StringReader;

class InfixToPrefix{

    /** *************************************************
     * tokenize arithmetic expression.
     * @param expr String represention the arithmetic string.
     * @return an iterator returnning each token in expr.
     * src: http://stackoverflow.com/questions/16498649/advanced-tokenizer-for-a-complex-math-expression
     *
     * TODO: doesn't handle slash (division) sign.
     * ************************************************** */
    public static List<String> tokenize(String expr) throws IOException{
        //for simple expression, use Java's built-in split().
        //for more complex, use StreamTokenizer instead of legacy StringTokenizer.
        StreamTokenizer tokenizer =
            new StreamTokenizer(new StringReader(expr));
        tokenizer.ordinaryChar('-');// Don't parse minus as part of numbers.

        List<String> tokBuf = new ArrayList<String>();
        while (tokenizer.nextToken() != StreamTokenizer.TT_EOF) {
            switch(tokenizer.ttype) {
                case StreamTokenizer.TT_NUMBER:
                    tokBuf.add(String.valueOf(tokenizer.nval));
                    break;
                case StreamTokenizer.TT_WORD:
                    tokBuf.add(tokenizer.sval);
                    break;
                default:  // operator
                    tokBuf.add(String.valueOf((char) tokenizer.ttype));
            }
        }
        return tokBuf;
    }

    //covert infix to prefix

    //driver/tester
    public static void main(String[] args){
        String str = "(8+2)+5*(6^2/1-8+2)";
        List<String> tokens = null;

        try{
            tokens = tokenize(str);
        } catch (IOException e){
            System.out.println(e);
        }

        for( String s : tokens ){
            System.out.println(s);
        }
    }
}

/*
Algorithm ConvertInfixtoPrefix
//Purpose: Convert an infix expression into a prefix expression. Begin

Create operand and operator stacks as empty stacks.
Create OperandStack
Create OperatorStack

// While input expression still remains, read and process the next token.
while( not an empty input expression ) read next token from the input expression

    // Test if token is an operand or operator
    if ( token is an operand )
        // Push operand onto the operand stack.
        OperandStack.Push (token)
    endif

    // If it is a left parentheses or operator of higher precedence than
    // the last, or the stack is empty,
    else if ( token is '(' or OperatorStack.IsEmpty() or OperatorHierarchy(token) > OperatorHierarchy(OperatorStack.Top()) ')
        // push it to the operator stack
        OperatorStack.Push ( token )
    endif

    else if( token is '')' )
        // Continue to pop operator and operand stacks, building
        // prefix expressions until left parentheses is found.
        // Each prefix expression is push back onto the operand
        // stack as either a left or right operand for the next operator.
        while( OperatorStack.Top() not equal '(' ')
            OperatorStack.Pop(operator)
            OperandStack.Pop(RightOperand)
            OperandStack.Pop(LeftOperand)
            operand = operator + LeftOperand + RightOperand
            OperandStack.Push(operand)
        endwhile

        // Pop the left parthenses from the operator stack.
        OperatorStack.Pop(operator)
    endif

    else if( operator hierarchy of token is less than or equal to hierarchy of top of the operator stack )
        // Continue to pop operator and operand stack, building prefix
        // expressions until the stack is empty or until an operator at
        // the top of the operator stack has a lower hierarchy than that
        // of the token.
        while( !OperatorStack.IsEmpty() and OperatorHierarchy(token) lessThen Or Equal to OperatorHierarchy(OperatorStack.Top()) )
            OperatorStack.Pop(operator)
            OperandStack.Pop(RightOperand)
            OperandStack.Pop(LeftOperand)
            operand = operator + LeftOperand + RightOperand
            OperandStack.Push(operand)
        endwhile
        // Push the lower precedence operator onto the stack
        OperatorStack.Push(token)
    endif
endwhile

// If the stack is not empty, continue to pop operator and operand stacks building
// prefix expressions until the operator stack is empty.
while( !OperatorStack.IsEmpty() ) OperatorStack.Pop(operator)
    OperandStack.Pop(RightOperand)
    OperandStack.Pop(LeftOperand)
    operand = operator + LeftOperand + RightOperand

    OperandStack.Push(operand)
endwhile

// Save the prefix expression at the top of the operand stack followed by
// popping the operand stack.
print OperandStack.Top()
OperandStack.Pop()

End Algorithm
*/
