package br.com.contmatic.teste;

public class Pessoa {

    private Integer idade;
    
    private String nome2;

    public Integer getIdade() {
        return idade;
    }

    public void setIdade(Integer idade) {
        this.idade = idade;
    }
    
    public String getNome() {
        return nome2;
    }

    public void setNome(String nome) {
        this.nome2 = nome;
    }

    @Override
    public String toString() {
        return "Pessoa [idade=" + idade + "]";
    }
    
}
