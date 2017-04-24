package br.com.contmatic.teste;

public class Pessoa {

    private Integer idade;

    public Integer getIdade() {
        return idade;
    }

    public void setIdade(Integer idade) {
        this.idade = idade;
    }

    @Override
    public String toString() {
        return "Pessoa [idade=" + idade + "]";
    }
    
}
