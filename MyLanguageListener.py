# Generated from MyLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete listener for a parse tree produced by MyLanguageParser.
class MyLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by MyLanguageParser#program.
    def enterProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#program.
    def exitProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#block.
    def enterBlock(self, ctx:MyLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#block.
    def exitBlock(self, ctx:MyLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#descriptionList.
    def enterDescriptionList(self, ctx:MyLanguageParser.DescriptionListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#descriptionList.
    def exitDescriptionList(self, ctx:MyLanguageParser.DescriptionListContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#nonEmptyTail.
    def enterNonEmptyTail(self, ctx:MyLanguageParser.NonEmptyTailContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#nonEmptyTail.
    def exitNonEmptyTail(self, ctx:MyLanguageParser.NonEmptyTailContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#emptyTail.
    def enterEmptyTail(self, ctx:MyLanguageParser.EmptyTailContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#emptyTail.
    def exitEmptyTail(self, ctx:MyLanguageParser.EmptyTailContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#simpleDesc.
    def enterSimpleDesc(self, ctx:MyLanguageParser.SimpleDescContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#simpleDesc.
    def exitSimpleDesc(self, ctx:MyLanguageParser.SimpleDescContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#arrayDesc.
    def enterArrayDesc(self, ctx:MyLanguageParser.ArrayDescContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#arrayDesc.
    def exitArrayDesc(self, ctx:MyLanguageParser.ArrayDescContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#simpleVarDescription.
    def enterSimpleVarDescription(self, ctx:MyLanguageParser.SimpleVarDescriptionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#simpleVarDescription.
    def exitSimpleVarDescription(self, ctx:MyLanguageParser.SimpleVarDescriptionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#typedArray.
    def enterTypedArray(self, ctx:MyLanguageParser.TypedArrayContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#typedArray.
    def exitTypedArray(self, ctx:MyLanguageParser.TypedArrayContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#logicArray.
    def enterLogicArray(self, ctx:MyLanguageParser.LogicArrayContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#logicArray.
    def exitLogicArray(self, ctx:MyLanguageParser.LogicArrayContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#type.
    def enterType(self, ctx:MyLanguageParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#type.
    def exitType(self, ctx:MyLanguageParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#identifierList.
    def enterIdentifierList(self, ctx:MyLanguageParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#identifierList.
    def exitIdentifierList(self, ctx:MyLanguageParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#nonEmptyTailId.
    def enterNonEmptyTailId(self, ctx:MyLanguageParser.NonEmptyTailIdContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#nonEmptyTailId.
    def exitNonEmptyTailId(self, ctx:MyLanguageParser.NonEmptyTailIdContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#emptyTailId.
    def enterEmptyTailId(self, ctx:MyLanguageParser.EmptyTailIdContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#emptyTailId.
    def exitEmptyTailId(self, ctx:MyLanguageParser.EmptyTailIdContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#bounds.
    def enterBounds(self, ctx:MyLanguageParser.BoundsContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#bounds.
    def exitBounds(self, ctx:MyLanguageParser.BoundsContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#statementList.
    def enterStatementList(self, ctx:MyLanguageParser.StatementListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#statementList.
    def exitStatementList(self, ctx:MyLanguageParser.StatementListContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#nonEmptyTailStmt.
    def enterNonEmptyTailStmt(self, ctx:MyLanguageParser.NonEmptyTailStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#nonEmptyTailStmt.
    def exitNonEmptyTailStmt(self, ctx:MyLanguageParser.NonEmptyTailStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#emptyTailStmt.
    def enterEmptyTailStmt(self, ctx:MyLanguageParser.EmptyTailStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#emptyTailStmt.
    def exitEmptyTailStmt(self, ctx:MyLanguageParser.EmptyTailStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#assignStmt.
    def enterAssignStmt(self, ctx:MyLanguageParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#assignStmt.
    def exitAssignStmt(self, ctx:MyLanguageParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#blockStmt.
    def enterBlockStmt(self, ctx:MyLanguageParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#blockStmt.
    def exitBlockStmt(self, ctx:MyLanguageParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#ifStmt.
    def enterIfStmt(self, ctx:MyLanguageParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#ifStmt.
    def exitIfStmt(self, ctx:MyLanguageParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#outputStmt.
    def enterOutputStmt(self, ctx:MyLanguageParser.OutputStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#outputStmt.
    def exitOutputStmt(self, ctx:MyLanguageParser.OutputStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#forStmt.
    def enterForStmt(self, ctx:MyLanguageParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#forStmt.
    def exitForStmt(self, ctx:MyLanguageParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#labelStmt.
    def enterLabelStmt(self, ctx:MyLanguageParser.LabelStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#labelStmt.
    def exitLabelStmt(self, ctx:MyLanguageParser.LabelStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#ifStatement.
    def enterIfStatement(self, ctx:MyLanguageParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#ifStatement.
    def exitIfStatement(self, ctx:MyLanguageParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#outputStatement.
    def enterOutputStatement(self, ctx:MyLanguageParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#outputStatement.
    def exitOutputStatement(self, ctx:MyLanguageParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#outputList.
    def enterOutputList(self, ctx:MyLanguageParser.OutputListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#outputList.
    def exitOutputList(self, ctx:MyLanguageParser.OutputListContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#nonEmptyTailOut.
    def enterNonEmptyTailOut(self, ctx:MyLanguageParser.NonEmptyTailOutContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#nonEmptyTailOut.
    def exitNonEmptyTailOut(self, ctx:MyLanguageParser.NonEmptyTailOutContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#emptyTailOut.
    def enterEmptyTailOut(self, ctx:MyLanguageParser.EmptyTailOutContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#emptyTailOut.
    def exitEmptyTailOut(self, ctx:MyLanguageParser.EmptyTailOutContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#forStatement.
    def enterForStatement(self, ctx:MyLanguageParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#forStatement.
    def exitForStatement(self, ctx:MyLanguageParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#step.
    def enterStep(self, ctx:MyLanguageParser.StepContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#step.
    def exitStep(self, ctx:MyLanguageParser.StepContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#labelStatement.
    def enterLabelStatement(self, ctx:MyLanguageParser.LabelStatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#labelStatement.
    def exitLabelStatement(self, ctx:MyLanguageParser.LabelStatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#varId.
    def enterVarId(self, ctx:MyLanguageParser.VarIdContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#varId.
    def exitVarId(self, ctx:MyLanguageParser.VarIdContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#varConst.
    def enterVarConst(self, ctx:MyLanguageParser.VarConstContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#varConst.
    def exitVarConst(self, ctx:MyLanguageParser.VarConstContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#varArray.
    def enterVarArray(self, ctx:MyLanguageParser.VarArrayContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#varArray.
    def exitVarArray(self, ctx:MyLanguageParser.VarArrayContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#arrayVariable.
    def enterArrayVariable(self, ctx:MyLanguageParser.ArrayVariableContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#arrayVariable.
    def exitArrayVariable(self, ctx:MyLanguageParser.ArrayVariableContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#index.
    def enterIndex(self, ctx:MyLanguageParser.IndexContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#index.
    def exitIndex(self, ctx:MyLanguageParser.IndexContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#constInt.
    def enterConstInt(self, ctx:MyLanguageParser.ConstIntContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#constInt.
    def exitConstInt(self, ctx:MyLanguageParser.ConstIntContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#constReal.
    def enterConstReal(self, ctx:MyLanguageParser.ConstRealContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#constReal.
    def exitConstReal(self, ctx:MyLanguageParser.ConstRealContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#constString.
    def enterConstString(self, ctx:MyLanguageParser.ConstStringContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#constString.
    def exitConstString(self, ctx:MyLanguageParser.ConstStringContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#constBool.
    def enterConstBool(self, ctx:MyLanguageParser.ConstBoolContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#constBool.
    def exitConstBool(self, ctx:MyLanguageParser.ConstBoolContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#expression.
    def enterExpression(self, ctx:MyLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#expression.
    def exitExpression(self, ctx:MyLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#binaryOp.
    def enterBinaryOp(self, ctx:MyLanguageParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#binaryOp.
    def exitBinaryOp(self, ctx:MyLanguageParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#emptyExprTail.
    def enterEmptyExprTail(self, ctx:MyLanguageParser.EmptyExprTailContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#emptyExprTail.
    def exitEmptyExprTail(self, ctx:MyLanguageParser.EmptyExprTailContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#fTail.
    def enterFTail(self, ctx:MyLanguageParser.FTailContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#fTail.
    def exitFTail(self, ctx:MyLanguageParser.FTailContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#condition.
    def enterCondition(self, ctx:MyLanguageParser.ConditionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#condition.
    def exitCondition(self, ctx:MyLanguageParser.ConditionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#comparisonOp.
    def enterComparisonOp(self, ctx:MyLanguageParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#comparisonOp.
    def exitComparisonOp(self, ctx:MyLanguageParser.ComparisonOpContext):
        pass



del MyLanguageParser