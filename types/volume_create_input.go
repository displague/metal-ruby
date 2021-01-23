// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// VolumeCreateInput volume create input
//
// swagger:model VolumeCreateInput
type VolumeCreateInput struct {

	// hourly
	BillingCycle string `json:"billing_cycle,omitempty"`

	// customdata
	Customdata interface{} `json:"customdata,omitempty"`

	// description
	Description string `json:"description,omitempty"`

	// ams1, ewr1, nrt1, sjc1
	// Required: true
	Facility *string `json:"facility"`

	// locked
	Locked bool `json:"locked,omitempty"`

	// storage_1, storage_2
	// Required: true
	Plan *string `json:"plan"`

	// size
	// Required: true
	Size *int64 `json:"size"`

	// snapshot policies
	SnapshotPolicies *SnapshotPolicyInput `json:"snapshot_policies,omitempty"`
}

// Validate validates this volume create input
func (m *VolumeCreateInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateFacility(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validatePlan(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateSize(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateSnapshotPolicies(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *VolumeCreateInput) validateFacility(formats strfmt.Registry) error {

	if err := validate.Required("facility", "body", m.Facility); err != nil {
		return err
	}

	return nil
}

func (m *VolumeCreateInput) validatePlan(formats strfmt.Registry) error {

	if err := validate.Required("plan", "body", m.Plan); err != nil {
		return err
	}

	return nil
}

func (m *VolumeCreateInput) validateSize(formats strfmt.Registry) error {

	if err := validate.Required("size", "body", m.Size); err != nil {
		return err
	}

	return nil
}

func (m *VolumeCreateInput) validateSnapshotPolicies(formats strfmt.Registry) error {

	if swag.IsZero(m.SnapshotPolicies) { // not required
		return nil
	}

	if m.SnapshotPolicies != nil {
		if err := m.SnapshotPolicies.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("snapshot_policies")
			}
			return err
		}
	}

	return nil
}

// MarshalBinary interface implementation
func (m *VolumeCreateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *VolumeCreateInput) UnmarshalBinary(b []byte) error {
	var res VolumeCreateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
