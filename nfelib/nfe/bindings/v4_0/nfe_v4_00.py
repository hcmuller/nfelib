"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:19

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import Tnfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Nfe(Tnfe):
    """
    Nota Fiscal Eletrônica.
    """

    class Meta:
        name = "NFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
