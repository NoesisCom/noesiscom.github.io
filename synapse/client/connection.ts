import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import { SynapseCore } from "../target/types/synapse_core";

const provider = anchor.AnchorProvider.env();
anchor.setProvider(provider);

const program = anchor.workspace.SynapseCore as Program<SynapseCore>;

export const sync_synapse = async () => {
    // establishing the neural link to the chain
    const tx = await program.methods.initialize().rpc();
    console.log("synapse_active: signal_confirmed", tx);
};
