ContractIdeas = """We want to create a bunch of solidity smart contracts. To do this, we need a large number of smart contracts with very simple but varied mechanisms. Some very basic ideas are smart contracts that: act like a vending machine for ERC-20 tokens, let the users play a game like Bop It, a simple collateralized borrowing contract, a simple token trading contract, a contract that lets users play tic tac toe, etc. Can you give some examples of ideas for smart contracts? . For each idea, please provide a paragraph that gives detailed instructions of how the smart contract would work.
1."""

CreateContract = f"""Please generate a solidity contract with pragma ^0.8.0 based on the description below. If the instructions are unclear, please do your best to try to implement the best version of the overall idea.

Idea: """
    
magicSearcher1 = '''
$ forge build 
Error:
Compiler run failed
src/Counter.sol:10:22: ParserError: Expected '=>' but got '='
    mapping (address => uint256) public balance;
                     ^
$ magic-searcher src/Counter.sol
Magic Searcher v1.0 for Mac - AI powered bash code generator - searches for relevant context to fix the error!
It looks like you can use the "cat" and "sed" commands to search for the relevant lines.
You can search for relevant code lines with the following command:
cat -n src/Counter.sol | sed -n 7,12p
$ forge build 
Error:
Compiler run failed
src/tic-tac-toe-game.sol:66:13: TypeError: "send" and "transfer" are only available for objects of type "address payable", not "address".
            player1.transfer(amount);
            ^--------------^
$ magic-searcher src/tic-tac-toe-game.sol
Magic Searcher v1.0 for Mac - AI powered bash code generator - searches for relevant context to fix the error!
It looks like you can use the "grep" command to search for the relevant lines (such as the definition of "player1").
You can search for relevant code lines with the following command:
grep -n -E "address.*player1|player1.*address" ./src/tic-tac-toe-game.sol
'''

magicSearcher2 ='''
$ forge build
Error: 
Compiler run failed
error[5796]: SyntaxError: Functions are not allowed to have the same name as the contract. If you intend this to be a constructor, use "constructor(...) { ... }" to define it.
  --> src/Counter.sol:13:3:
   |
13 |   function PredictionMarket() public {
   |   ^ (Relevant source part starts here and spans across multiple lines).
$ magic-searcher src/Counter.sol
Magic Searcher v1.0 for Mac - AI powered bash code generator - searches for relevant context to fix the error!
It looks like you can use "sed" command to search for the relevant lines.
You can search for relevant code lines with the following command:
cat -n src/Counter.sol | sed -n 11,15p
$ forge build
Error:
Compiler run failed
error[9478]: ParserError: Expected string literal (path), "*" or alias list.
 --> src/Pool/Pool.sol:3:8:
  |
3 | import "./PoolImports.sol; /*
  |        ^^^^^^^^^^^^^^^^^^^^^
$ magic-searcher src/Pool/Pool.sol
Magic Searcher v1.0 for Mac - AI powered bash code generator - searches for relevant context to fix the error!
It looks like you need to use the "cat" and "sed" commands to search for the relevant lines.
You can search for relevant code lines with the following command:
$ cat -n ./src/Pool/Pool.sol | sed -n 1,5p
'''

prefix = \
"$ cd ../Counter.sol" +\
'''
$ forge build 
Error:
Compiler run failed
'''

promptPrefix = '''
$ forge build 
Error:
Compiler run failed
src/tic-tac-toe-game.sol:66:13: TypeError: "send" and "transfer" are only available for objects of type "address payable", not "address".
            player1.transfer(amount);
            ^--------------^
$ magic-searcher src/tic-tac-toe-game.sol
Magic Searcher v1.0 - AI powered bash code generator - searches for relevant context to fix the error!
It looks like you need to use "grep" command to search for the relevant lines.
You can search for relevant code lines with the following command:
$ grep -n -E "address.*player1|player1.*address" ./src/

$ grep -n -E "address.*player1|player1.*address" ./src/
tic-tac-toe-game.sol
5:    address public player1;
16:        player1 = address(0);
28:        if (player1 == address(0)) \{
36:        require(player1 != address(0) && player2 != address(0), "Two players must exist.");
$ magic-patcher ./src/
tic-tac-toe-game.sol
Magic Patcher v1.5 for Mac - AI powered bug fixer - fixes all bugs!

It looks like the variable player1 is of type address instead of address payable. You can fix it with the following command:
sed -i '' 's/address public player1;/address payable public player1;/g' src/tic-tac-toe-game.sol
''' + \
"$ cd ../project_name" +\
'''
$ forge build 
Error:
Compiler run failed
'''

magicSearcherPostfix = f'''$ magic-searcher ./src/Counter.sol
Magic Searcher v1.5 for Mac  - AI powered bash code generator - searches for relevant context to fix the error!'''

magicPatcherPostfix = f'''$ magic-patcher ./src/Counter.sol
Magic Patcher v1.5 for Mac - AI powered bug fixer - fixes all bugs!'''
