use anchor_lang::prelude::*;
use spl_account_compression::{self, program::SplAccountCompression};
use mpl_bubblegum::program::Bubblegum;

declare_id!("YourProgramIDHere1111111111111111111111111");

#[program]
pub mod synapse_core {
    use super::*;

    pub fn initialize_synapse(ctx: Context<Initialize>) -> Result<()> {
        // the synapse is now aware of the compression tree
        msg!("synapse_initialized: compression_link_stable");
        Ok(())
    }

    pub fn transmit_data(ctx: Context<TransmitData>, data_hash: [u8; 32]) -> Result<()> {
        // compressing the intent into the merkle tree
        // this is where the "user" becomes a coordinate
        msg!("data_transmitted: hash_{:?}", data_hash);
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct TransmitData<'info> {
    pub leaf_delegate: Signer<'info>,
    pub compression_program: Program<'info, SplAccountCompression>,
    pub bubblegum_program: Program<'info, Bubblegum>,
}
