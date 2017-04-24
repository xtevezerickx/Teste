package br.com.contmatic.teste;

import org.junit.Assert;
import org.junit.Test;


public class Teste {
    
    @Test
    public void idade_pessoa_deve_ser_maior_ou_igual_a_18(){
        Pessoa pessoa = new Pessoa();
        pessoa.setIdade(18);
        Assert.assertTrue(pessoa.getIdade() >= 18);
    }
}
